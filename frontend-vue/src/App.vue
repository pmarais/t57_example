<template>
  <Header title="This is hello world"/>
  <Urls @delete-url="deleteUrl" :urls="urls"/>
</template>

<script>
import Header from './components/Header.vue'
import Urls from './components/Urls.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Header,
    Urls,
  },
  data () {
    return {
      urls: []
    }
  },
  created () {
    axios.get('http://localhost:8000/api/urls/').then(response => {
      this.urls = response.data
      // console.log(response.data)
      // console.log(this.urls)
    })
  },
  methods: {
    deleteUrl (id) {
      console.log('delete-url', id)
      axios.delete(`http://localhost:8000/api/urls/${id}/`).then(response => {
        this.urls = this.urls.filter((url) => url.id !== id) // keep verything that isn't the deleted item
      })
    }
  },
  mounted () {
    // console.log(this.urls)
  }
}
</script>

<style>
@import './assets/base.css';

#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;

  font-weight: normal;
}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

a,
.green {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.4s;
}

@media (hover: hover) {
  a:hover {
    background-color: hsla(160, 100%, 37%, 0.2);
  }
}

@media (min-width: 1024px) {
  body {
    display: flex;
    place-items: center;
  }

  #app {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  }

  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  .logo {
    margin: 0 2rem 0 0;
  }
}
</style>

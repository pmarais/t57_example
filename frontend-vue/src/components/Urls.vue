<template>
<p></p>
  <input type="text" name="newurl" v-model="newUrl" /> 
  <button @click="submit()" type="">Add new</button>
  <ul>
    <li :key="item.id" v-for="(item, index) in urls">
      <Url @delete-url="$emit('delete-url', item.id)" :url="item" />
    </li>  
  </ul>
</template>

<script>
import axios from 'axios'
  import Url from './Url.vue'

  export default {
    name: 'Urls',
    props: {
      urls: Array,
    },
    components: {
      Url
    },
    emits: ['delete-url',],
    data () {
      return {
        newUrl: '',
        editUrl: '',
      }
    },
    methods: {
      async getUrl (id) {
        const response = await axios.get(`http://localhost:8000/api/urls/${id}`)
        const data = await response.data
      },
      async submit() {
        const submitObj = {u_url: this.newUrl}
        // console.log(submitObj)
        const response = await axios.post('http://localhost:8000/api/urls/', submitObj)
        const data = await response.data
        this.urls.push(response.data)
        this.newUrl = ''
      },
      async submitEdit () {
        console.log('editing')
      }
    }
  }
</script>
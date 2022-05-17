<template>
  <div :key="item.id" v-for="(item, index) in urls">
    <Url @delete-url="$emit('delete-url', item.id)" :url="item" />
  </div>
</template>

<script>
  import Url from './Url.vue'

  export default {
    name: 'Urls',
    props: {
      urls: Array,
    },
    components: {
      Url
    },
    emits: ['delete-url',]
  }
</script>
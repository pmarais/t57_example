<template>
  <h3> {{url.id}} — <a target="_blank" :href="url.u_url">{{url.u_url}}</a> <button @click="$emit('delete-url', url.id)">Delete</button></h3>
</template>

<script>
  export default {
    name: "Url",
    props: {
      url: Object,
    },
    emits: ['delete-url',]
  }
</script>
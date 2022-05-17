<template>
  <button @click="onClick()" class="btn"> {{text}} </button>
</template>

<script>
export default {
  name: "Button",
  props: {
    text: String,
  },
  methods: {
    onClick () {
      console.log('here')
    }
  }
}
</script>
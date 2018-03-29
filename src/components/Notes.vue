<template>
  <Directory title="Notes" :items="items"></Directory>
</template>

<script>
import Directory from './Directory.vue'

export default {
  name: 'notes',
  props: [],
  data () {
    return {
      items: [
        {
          name: "COMP3131",
          link: "http://thefuckifiknow.com",
          sub: "i'm more of a dom",
          count: 7
        },
        {
          name: "COMP2121",
          link: "http://thefuckifiknow.com",
          sub: "lmao",
          count: 9
        },
        {
          name: "COMP38fuck2",
          link: "http://thefuckifiknow.com",
          sub: "i know, genius",
          count: 23
        }
      ]
    }
  },
  methods: {},
  components: {
    Directory
  }
}
</script>

<style>
body {
    background-color: #272B30;
}
</style>

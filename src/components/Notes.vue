<template>
  <div>
    <Directory v-if="this.state == 'dir'" :title="title" :items="items"></Directory>
    <MarkdownPage v-if="this.state == 'file'" :content="renderedMd" :title="title"> </MarkdownPage>
  </div>
</template>

<script>
import Directory from './Directory.vue'
import MarkdownPage from './MarkdownPage.vue'
import axios from 'axios';

export default {
  name: 'notes',
  props: [],
  data () {
    return {
      title: "Notes",
      items: [],
      errors: [],
      state: "dir",
      renderedMd: null,
      base: "http://127.0.0.1:5000"
    }
  },
  watch: {
    $route (to, from){
        if (!this.$route.params.file) this.updateItems()
        else this.renderMd()
    }
  },
  created() {
    if (!this.$route.params.file) this.updateItems()
    else this.renderMd()
  },
  methods: {
    updateItems: function() {
      this.state = "dir"
      let url = this.base
      if(this.$route.params.course) {
        url += "/notesapi/"+this.$route.params.course
        this.title = this.$route.params.course
      }else{
        url += "/notesapi"
      }
      axios.get(url).then(result => {
        this.items = result.data
      }).catch(err => {
          this.errors.push(err)
      })
    },
    renderMd: function() {
      this.state = "file"
      this.title = this.$route.params.file
      let url = this.base + "/notesapi/"
      url += this.$route.params.course+"/"+this.$route.params.file
      this.renderedMd = null

      axios.get(url).then(result => {
        this.renderedMd = result.data
      }).catch(err => {
        this.errors.push(err)
      })
    }
  },
  components: {
    Directory,
    MarkdownPage
  }
}
</script>

<style>
body {
    background-color: #272B30;
}
</style>

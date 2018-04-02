<template>
  <div class="md-page">
    <div class="md-page-title">
      <h1> {{title}} </h1>
      <hr>
    </div>
    <div class="md-page-content">
      <div v-if="content == null">
        <pulse-loader :loading="loading" color="#919aa1"></pulse-loader>
      </div>
      <div v-if="content != null">
        <h1 style="color: white"> BITCH! </h1>
      </div>
    </div>
  </div>
</template>

<script>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: 'markdownPage',
  props: ["content","title"],
  data () {
    return {}
  },
  components: {
    PulseLoader
  }
}
</script>

<style>
/*
 * Frankly a bit of a hack copying the hex color
 * theme should be universal
 */
.md-page {
  width: 100vw;
  text-align: center;
  font-family: 'Ubuntu',sans-serif;
}
.md-page .md-page-title {
    padding-top: 10vh;
    color: white;
}
.md-page hr{
  border: 0;
  height: 3px;
  width: 60%;
  border-radius: 25px;
  background-color: #919aa1;
}

.md-page h1{
  font-size: 2.5rem;
  margin-top: 0;
}

.md-page .md-page-content {
  margin-top: 4em;
}
</style>

<template>
  <div class="dir">
    <div class="dir-title">
      <h1> {{title}} </h1>
      <hr id="title-ul">
    </div>
    <div class="items-container">
      <div v-for="i in items"><Item :data="i"></Item></div>
    </div>
  </div>
</template>

<script>
import Item from './Item.vue'
export default {
  name: 'directory',
  props: ["title","items"],
  data () {
    return {}
  },
  methods: {},
  components: {
    Item
  }
}
</script>

<style>
/*
 * Frankly a bit of a hack copying the hex color
 * theme should be universal
 */
.dir {
  width: 100vw;
  text-align: center;
  font-family: 'Ubuntu',sans-serif;
}
.dir .dir-title {
    padding-top: 15vh;
    color: white;
}
.dir hr{
  border: 0;
  height: 3px;
  width: 60%;
  border-radius: 25px;
  background-color: #919aa1;
}

.dir h1{
  font-size: 3rem;
  margin-top: 0;
}
.dir .items-container {
  margin-left: 20%;
  margin-right: 20%;
  padding: 2em;
}
</style>

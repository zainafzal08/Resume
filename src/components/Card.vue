<template>
  <div :id="name" class="poster-card shadow" :style="{'background-color': bgc}">
    <div class="innards" :id="name+'-innards'">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: ["name","bgc"],
  data () {
    return {}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .poster-card {
    width: 100vw;
    height: 100vh;
  }

  /* actual card components */
  .poster-card .innards{
    width: 100%;
    height: 100%;
    font-family: 'Ubuntu', sans-serif;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>

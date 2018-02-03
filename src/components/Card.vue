<template>
  <div>
    <div v-if="bgt == 'color'" :id="name" class="poster-card shadow" :style="{'background-color': bg}">
      <div class="innards" :id="name+suffix">
        <slot></slot>
      </div>
    </div>
    <div v-if="bgt == 'image'" :id="name" class="poster-card shadow back-img" :style="{'background-image': 'url('+bg+')'}">
      <div class="innards" :id="name+suffix">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Card',
  props: ["name","bg","bgt","suffix"],
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

  /* poster background info */
  .back-img {
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
  }

</style>

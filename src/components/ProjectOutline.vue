<template>
  <div class="project">
    <div class="top">
      <h1> Web Scraping Scripts </h1>
    </div>
    <div class="bottom">
      <div class="panels">
        <div class="panel">
          <h1> DICKS </h1>
        </div>
        <div class="panel">
          <h1> BUTTS </h1>
        </div>
        <div class="panel">
          <h1> DICKS AND BUTTS </h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectOutline',
  props: ["title"],
  data () {
    return {

    }
  },
  methods: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .project {
    width: 100vw;
    height: 100vh;
    background-color: rgba(44,62,80,0.5);
  }

  .project .top {
    width: 100%;
    height: 40%;
    display: flex;
  }
  .project .bottom {
    width: 100%;
    height: 60%;
  }
  .project .panels {
    margin-left: 10%;
    width: 90%;
    height: 100%;
    display: flex;
    flex-direction: row;
  }
  .project .panels .panel {
    width: 32%;
    margin-left: 1%;
    height: 80%;
    text-align: center;
  }
</style>

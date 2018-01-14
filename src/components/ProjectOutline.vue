<template>
  <div class="project">
    <h1> {{title}} </h1>
    <hr>
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
    width: 40vw;
    text-align: center;
  }

  .project hr{
    border: 0;
    height: 3px;
    border-radius: 25px;
    width: 100%;
    background-color: white;
  }

  .project h1{
    font-size: 3rem;
  }
  .project h3{
    font-size: 1.5rem;
    color: #919aa1;
    padding: 0;
    margin: 0;
    width: 100%;
  }
</style>

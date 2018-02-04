<template>
  <div class="project-container">
    <div class="project" :style="{'background-color': calcBg(bg,0.55)}">
      <div class="title">
        <h1>{{title}}</h1>
      </div>
      <div class="content shadow" :style="{'border-color': theme, 'background-color': bg}">
        <div class="container">

          <div v-for="(point, i) in points">
            <ProjectElem :title="point.title" :description="point.description" :theme="theme" :links="point.links"></ProjectElem>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProjectElem from './ProjectElem.vue'

export default {
  name: 'ProjectOutline',
  props: ["title", "bg", "theme", "points"],
  data () {
    return {}
  },
  components: {
    ProjectElem
  },
  methods: {
    calcBg(color,o) {
      let r = parseInt(color.substring(1,3),16);
      let g = parseInt(color.substring(3,5),16);
      let b = parseInt(color.substring(5,7),16);
      return "rgba("+r+","+g+","+b+","+o+")";
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Raleway|Nunito|Josefin+Sans');
  .project-container {
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: flex-end;
  }

  .project {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .project .title {
    width: 100vw;
    height: 30vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }

  .project .title h1 {
    font-family: 'josefin sans', monospace;
    font-size: 4rem;
    margin: 0;
  }

  .project .content {
    width: 60vw;
    height: 70vh;
    border-top: 3px solid;
  }
  .project .content .container{
    margin: 3rem;
    display: flex;
    flex-direction: column;
  }

  @media screen and (max-width: 600px){
    .project .content {
      width: 100vw;
      height: 70vh;
      border-top: 3px solid;
    }
    .project .title h1 {
      font-family: 'josefin sans', monospace;
      font-size: 3rem;
      margin: 0;
    }
    .project .content .container{
      margin: 3rem;
      margin-top: 2rem;
      display: flex;
      flex-direction: column;
    }
  }

  @media screen and (min-width: 1500px){
    .project .content {
      width: 50vw;
      height: 70vh;
      border-top: 3px solid;
    }
    .project .title h1 {
      font-family: 'josefin sans', monospace;
      font-size: 5rem;
      margin: 0;
    }
    .project .content .container{
      margin: 3rem;
      display: flex;
      flex-direction: column;
    }
  }
  .shadow {
      box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
  }
</style>

<template>
  <div class="project-container">
    <div class="project" :style="{'background-color': calcBg(bg,0.55)}">
      <div class="title">
        <h1>{{title}}</h1>
      </div>
      <div class="content shadow" :style="{'border-color': theme, 'background-color': bg}">
        <div class="container">

          <div v-for="point in points">
            <div class="elem">
              <div class="elem-title">
                <h2> {{point.title}} </h2>
              </div>
              <div class="description">
                <div class="links" :style="{'border-color': theme}">
                  <a class="mdi mdi-github-circle" :href="point.link"></a>
                </div>
                <div class="text">
                  <p>
                    {{point.description}}
                  </p>
                </div>
              </div>
            </div>
            <br><br>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectOutline',
  props: ["title", "bg", "theme", "points"],
  data () {
    return {

    }
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
  }

  /* Elem */
  .project .content .elem {
    width: 100%;
    height: 7rem;
    display: flex;
    flex-direction: column;
  }

  .project .content .elem .elem-title{
    width: 100%;
    height: 40%;
  }

  .project .content .elem .elem-title h2{
    font-family: 'josefin sans', monospace;
    margin: 0;
    font-size: 1.5rem;
  }

  .project .content .elem .description{
    width: 100%;
    height: 60%;
    display: flex;
    flex-direction: row;
  }

  .project .content .elem .description .links{
    height: 100%;
    border-right: solid 2px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .project .content .elem .description .links a{
    font-size: 2.6rem;
    margin-bottom: 0.9rem;
    opacity: 0.4;
    align-self: left;
    cursor: pointer;
    color: white;
    margin-right: 1rem;
  }
  .project .content .elem .description .links a:hover{
    opacity: 1;
  }
  .project .content .elem .description .text{
    height: 100%;
  }
  .project .content .elem .description .text p{
    margin-left: 5%;
  }
  @media screen and (max-width: 600px){

  }

  .shadow {
      box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
  }
</style>

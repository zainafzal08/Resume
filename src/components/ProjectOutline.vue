<template>
  <div class="project-container">
    <div class="project" :style="{'background-color': calcBg(bg,0.55)}">
      <div class="title">
        <h1>{{title}}</h1>
      </div>
      <div class="content shadow" :style="{'border-color': theme, 'background-color': bg}">
        <div class="container">

          <div v-for="(point, i) in points">
            <div class="elem">
              <div class="elem-title">
                <h2> {{point.title}} </h2>
              </div>
              <div class="description">
                <div :id="getContainId(title,i)" class="links" :style="{'border-color': theme}">
                  <a :id="getLinkId(title,i)" class="mdi mdi-format-horizontal-align-right" v-on:click="toggleLink(title,i)"></a>
                </div>
                <div class="text">
                  <p :id="getContentId(title,i)">
                    {{point.description}}
                  </p>
                </div>
              </div>
            </div>
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
      toggleState: (new Array(this.points.length)).fill(false),
      animating: (new Array(this.points.length)).fill(false)
    }
  },
  methods: {
    calcBg(color,o) {
      let r = parseInt(color.substring(1,3),16);
      let g = parseInt(color.substring(3,5),16);
      let b = parseInt(color.substring(5,7),16);
      return "rgba("+r+","+g+","+b+","+o+")";
    },
    toggleLink(t,i) {
      if (this.animating[i]) {
        return
      }
      let container = document.getElementById(this.getContainId(t,i));
      let content = document.getElementById(this.getContentId(t,i));
      let link = document.getElementById(this.getLinkId(t,i));
      this.toggleState[i] = !this.toggleState[i];
      if (this.toggleState[i]) {
        this.animating[i] = true;
        setTimeout(function(){this.animating[i] = false}.bind(this,i),1050);
        // expand
        window.Velocity(container, {'padding-right': '90%'}, 1000);
        window.Velocity(content, {'opacity': '0'}, 200);
        window.Velocity(link, {rotateZ: '180deg'}, 500);
      } else {
        this.animating[i] = true;
        setTimeout(function(){this.animating[i] = false}.bind(this,i),1050);
        // collapse
        window.Velocity(container, {'padding-right': '0%'}, 1000);
        window.Velocity(link, {rotateZ: '0deg'}, 500);
        setTimeout(function () {
          window.Velocity(content, {'opacity': '1'}, 200);
        }.bind(content), 800);
      }
    },
    getContainId(t,i) {
      t = t.replace(' ','-');
      return t+'-'+i;
    },
    getLinkId(t,i) {
      t = t.replace(' ','-');
      return t+'-'+i+'-link';
    },
    getContentId(t,i) {
      t = t.replace(' ','-');
      return t+'-'+i+'-content';
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

  /* Elem */

  .project .content .elem {
    height: 7rem;
    display: flex;
    flex-direction: column;
    margin-bottom: 2rem;
  }

  .project .content .elem .elem-title{
    height: 40%;
  }

  .project .content .elem .elem-title h2{
    font-family: 'josefin sans', monospace;
    margin: 0;
    font-size: 1.5rem;
  }

  .project .content .elem .description{
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
    display: flex;
    align-items: center;
  }
  .project .content .elem .description .text p{
    margin-left: 5%;
    margin-top: 0;
    margin-bottom: 0;
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
    .project .content .elem {
      height: 7rem;
      display: flex;
      flex-direction: column;
      margin-bottom: 3.5rem;
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
    .project .content .elem {
      height: 7rem;
      display: flex;
      flex-direction: column;
      margin-bottom: 6rem;
    }
  }
  .shadow {
      box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
  }
</style>

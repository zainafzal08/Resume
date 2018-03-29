<template>
  <div class="elem">
    <div class="elem-title">
      <h2> {{title}} </h2>
    </div>
    <div class="description">
      <div class="open-button" :style="{'border-color': theme}">
        <div v-for="link in links">
          <a :href="link.link" :class="'mdi mdi-'+link.icon"></a>
        </div>
      </div>
      <div class="text">
        <p :id="getContentId(title)">
          {{description}}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectElem',
  props: ['title','description','theme', 'links'],
  data () {
    return {
      animating: false,
      toggled: false
    }
  },
  methods: {
    toggleLink(t) {
      if (this.animating) {
        return
      }
      let container = document.getElementById(this.getContainId(t));
      let content = document.getElementById(this.getContentId(t));
      let link = document.getElementById(this.getLinkButtonId(t));
      let icons = document.getElementById(this.getLinksId(t)).childNodes;
      this.toggled = !this.toggled;
      if (this.toggled) {
        this.animating = true;
        setTimeout(function(){this.animating = false}.bind(this),800);
        // expand
        window.Velocity(container, {'width': '100%'}, 800);
        window.Velocity(content, {'opacity': '0'}, 200);
        window.Velocity(link, {rotateZ: '180deg'}, 500);
      } else {
        this.animating = true;
        setTimeout(function(){this.animating = false}.bind(this),800);
        // collapse
        window.Velocity(link, {rotateZ: '0deg'}, 500);
        window.Velocity(container, {'width': '0%'}, 800);
        setTimeout(function() {
          window.Velocity(content, {'opacity': '1'}, 200);
        },200);
      }
    },
    getContainId(t) {
      t = t.replace(' ','-');
      return t+'-container';
    },
    getLinkButtonId(t) {
      t = t.replace(' ','-');
      return t+'-link-button';
    },
    getLinksId(t) {
      t = t.replace(' ','-');
      return t+'-links';
    },
    getContentId(t) {
      t = t.replace(' ','-');
      return t+'-content';
    }
  }
}
</script>

<style>
  .hidden {
    opacity: 0;
    display: none;
  }
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

  .project .content .elem .description .open-button {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: solid 2px;
  }

  .project .content .elem .description a{
    font-size: 2.6rem;
    opacity: 0.4;
    cursor: pointer;
    color: white;
    margin-right: 1rem;
  }
  .project .content .elem .description a:hover{
      opacity: 1;
  }

  .project .content .elem .description .links a{
    color: white;
  }

  .project .content .elem .description .text{
    height: 100%;
    display: flex;
    align-items: center;
    font-family: 'Ubuntu';
  }
  .project .content .elem .description .text p{
    margin-left: 5%;
    margin-top: 0;
    margin-bottom: 0;
  }
  @media screen and (max-width: 600px){
    .project .content .elem {
      height: 7rem;
      display: flex;
      flex-direction: column;
      margin-bottom: 2rem;
    }
    .project .content .elem .description .text{
      height: 100%;
      display: flex;
      align-items: center;
      font-size: 0.9rem;
    }
    .project .content .elem .elem-title h2{
      font-family: 'josefin sans', monospace;
      margin: 0;
      font-size: 1.3rem;
    }
  }

  @media screen and (min-width: 1500px){
    .project .content .elem {
      height: 7rem;
      display: flex;
      flex-direction: column;
      margin-bottom: 6rem;
    }
    .project .content .elem .description .text{
      height: 100%;
      display: flex;
      align-items: center;
      font-size: 1.2rem;
    }
    .project .content .elem .elem-title h2{
      font-family: 'josefin sans', monospace;
      margin: 0;
      font-size: 1.8rem;
    }
  }
</style>

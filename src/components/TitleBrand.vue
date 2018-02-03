<template>
  <div class="brand">
    <h1> {{title}} </h1>
    <hr id="title-ul">
    <div class="tag-lines">
        <div v-for="(tag,i) in tagLines" class="tag" :id="'tag-'+i">
          <h3 :id="'tag-'+i+'-contents'" :style="{'color': tag.color}" v-html="tag.text"></h3>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TitleBrand',
  props: ["title","colors"],
  data () {
    return {
      tagCycler: null,
      tagLines: [
        {
          text: "Student &#8226; Developer &#8226; Nerd",
          color: "#919aa1"
        },
        {
          text: "A real whizz with html",
          color: this.colors[0]
        },
        {
          text: "Hair insured for $10,000",
          color: this.colors[1]
        },
        {
          text: "Loves python like a child",
          color: this.colors[2]
        },
        {
          text: "Only cries a little at seg faults",
          color: this.colors[3]
        }
      ],
      liveTag: 0
    }
  },
  methods: {
    cycleTagLines() {
      if (this.liveTag == this.tagLines.length-1) {
        this.liveTag = 0
        this.resetTagLines()
        return
      }
      // get our elements
      let ul = document.getElementById("title-ul")
      let ti = this.liveTag
      let t = document.getElementById("tag-"+ti)
      let tc = document.getElementById("tag-"+ti+"-contents")
      window.Velocity(t, {'min-width': '0%'}, 1000)
      window.Velocity(ul, {'background-color': this.tagLines[ti+1].color}, 1000)
      window.Velocity(tc, {'opacity':'0'}, 500)
      this.liveTag++
    },
    resetTagLines() {
      let ul = document.getElementById("title-ul")
      window.Velocity(ul, {'background-color': this.tagLines[0].color}, 1000)
      for (var i in this.tagLines) {
        let t = document.getElementById("tag-"+i)
        let tc = document.getElementById("tag-"+i+"-contents")
        window.Velocity(t, {'min-width': '100%'}, 500)
        window.Velocity(tc, {'opacity':'1'}, 1000)
      }
    }
  },
  created () {
    this.tagCycler = window.setInterval(this.cycleTagLines, 5000)
  },
  destroyed () {
    window.clearInterval(this.tagCycler);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Roboto|Source+Sans+Pro|Ubuntu');

  .brand {
    width: 40vw;
    text-align: center;
    font-family: 'Ubuntu',sans-serif;
  }

  .brand hr{
    border: 0;
    height: 3px;
    border-radius: 25px;
    width: 100%;
    background-color: #919aa1;
  }

  .brand h1{
    font-size: 3rem;
    margin-top: 0;
  }
  .brand h3{
    font-size: 1.5rem;
    color: #919aa1;
    padding: 0;
    margin: 0;
    width: 100%;
  }

  /* roles animations */
  .brand .tag-lines {
    margin-top: 1.5rem;
    width: 100%;
    height: 1.7rem;
    overflow: hidden;
    display: flex;
    flex-direction: row;
  }

  .brand .tag-lines .tag {
    min-width: 100%;
  }

  @media screen and (max-width: 600px){
    .brand {
      width: 90vw;
      text-align: center;
      font-family: 'Ubuntu',sans-serif;
    }

  }
</style>

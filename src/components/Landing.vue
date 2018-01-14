<template>
  <div class="poster-container">
    <!-- With < max elements they need to hover near middle -->

    <div id="nav-dots" class="nav-dots">
      <div class="dots">
        <div v-for="c in numCards" class="dot">
          <a class="mdi mdi-checkbox-blank-circle-outline" v-if="card != c" v-on:click="updateCard(c)"></a>
          <a class="mdi mdi-checkbox-blank-circle" v-if="card == c"></a>
        </div>
      </div>
    </div>

    <div id ="card-1" class="poster-card poster-1 shadow">
      <div class="innards" id="card-1-innards">
        <div class="brand">
          <h1> Zain Afzal </h1>
          <hr id="title-ul">
          <div class="tag-lines">
              <div v-for="(tag,i) in tagLines" class="tag" :id="'tag-'+i">
                <h3 :id="'tag-'+i+'-contents'" :style="{'color': tag.color}" v-html="tag.text"></h3>
              </div>
          </div>
        </div>
      </div>
    </div>

    <div id ="card-2" class="poster-card poster-2 shadow">
      <div class="innards" id="card-2-innards">

      </div>
    </div>
    <div id ="card-3" class="poster-card poster-3 shadow">
      <div class="innards" id="card-3-innards">

      </div>
    </div>
  </div>
</template>

<script>
import './js/velocity.js'

export default {
  name: 'Landing',
  data () {
    return {
      animating: false,
      card: 1,
      numCards: 3,
      scrollThreshold: 15,
      tagCycler: null,
      tagLines: [
        {
          text: "Student &#8226; Developer &#8226; Nerd",
          color: "#919aa1"
        },
        {
          text: "A real whizz with html",
          color: "#d9534f"
        },
        {
          text: "Hair insured for $10,000",
          color: "#29ABE0"
        },
        {
          text: "Loves python like a child",
          color: "#F47C3C"
        },
        {
          text: "Only cries a little at seg faults",
          color: "#93C54B"
        }
      ],
      liveTag: 0
    }
  },
  methods: {
    handleScroll (e) {
      if (e.deltaY > this.scrollThreshold && this.card < this.numCards ) {
        this.nextCard(800,false)
      }
      if (e.deltaY < -1 * this.scrollThreshold  && this.card > 1 ) {
        this.prevCard(800,false)
      }
    },
    updateCard(c) {
      let adjust = (this.card > c) ? 1 : -1
      let target = this.card
      while(c != target) {
        if (adjust == 1) {
          this.prevCard(500,true)
        } else {
          this.nextCard(500,true)
        }
        c += adjust
      }
    },
    nextCard (d,ignoreState) {
      if (this.animating && !ignoreState) {
        return
      } else if (!ignoreState) {
        this.animating = true
        setTimeout(function() { this.animating = false }.bind(this), d+100)
      }
      window.Velocity(document.getElementById('card-' + this.card), {'margin-top': '-100vh'}, d)
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '0'}, d)
      this.card++
    },
    prevCard (d,ignoreState) {
      if (this.animating) {
        return
      } else if (!ignoreState) {
        this.animating = true
        setTimeout(function() { this.animating = false }.bind(this), d+100)
      }
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '0'}, d)
      this.card--
      window.Velocity(document.getElementById('card-' + this.card), {'margin-top': '0vh'}, d)
      window.Velocity(document.getElementById('card-' + this.card + '-innards'), {opacity: '1'}, d)
    },
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
    window.addEventListener('wheel', this.handleScroll)
    this.tagCycler = window.setInterval(this.cycleTagLines, 5000)
  },
  destroyed () {
    window.removeEventListener('wheel', this.handleScroll)
    window.clearInterval(this.tagCycler);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Roboto|Source+Sans+Pro|Ubuntu');

  /* Container  */
  .poster-container {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }

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

  .poster-card .innards .brand {
    width: 40vw;
    text-align: center;
  }

  .poster-card .innards .brand hr{
    border: 0;
    height: 3px;
    border-radius: 25px;
    width: 100%;
    background-color: white;
  }
  .poster-card .innards .brand h1{
    font-size: 3rem;
  }
  .poster-card .innards .brand h3{
    font-size: 1.5rem;
    color: #919aa1;
    padding: 0;
    margin: 0;
    width: 100%;
  }

  /* roles animations */
  .poster-card .innards .tag-lines {
    margin-top: 1.5rem;
    width: 100%;
    height: 1.7rem;
    overflow: hidden;
    display: flex;
    flex-direction: row;
  }

  .poster-card .innards .tag-lines .tag {
    min-width: 100%;
  }

  /* nav bar */
  .poster-container .nav-dots {
    display: flex;
    width: 10vw;
    height: 100vh;
    position: absolute;
    left: 2rem;
    align-items: center;
  }


  .poster-container .nav-dots .dots{
    width: 100%;
    text-align: center;
    font-size: 1.8rem;
    color: white;
    display: flex;
    flex-direction: column;
  }

  .poster-container .nav-dots .mdi-checkbox-blank-circle-outline:hover {
    opacity: 0.5;
  }

  .poster-container .nav-dots .dots .dot {
    margin-bottom: 0.3rem;
  }

  @media screen and (max-width: 500px){
    .poster-container .nav-dots .dots{
      width: 100%;
      text-align: center;
      font-size: 1.5rem;
      color: white;
      display: flex;
      flex-direction: column;
    }
  }


  /* poster background info */
  .poster-1 {
    background: #272B30;
  }
  .poster-2 {
    background-image: url('./images/poster_1.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
  }
  .poster-3 {
    background: #444444;
  }

  /* material design shadows */
  .shadow {
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);
  }
</style>

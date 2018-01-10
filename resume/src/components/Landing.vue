<template>
  <div class="poster-container">
    <div id ="card-1" class="poster-card" :style="{background: '#444444'}">

    </div>
    <div id ="card-2" class="poster-card" :style="{background: '#00FF00'}">

    </div>
    <div id ="card-3" class="poster-card" :style="{background: '#0000FF'}">

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
      scrollThreshold: 15
    }
  },
  methods: {
    handleScroll (e) {
      if (e.deltaY > this.scrollThreshold && !this.animating && this.card < this.numCards) {
        this.animating = true
        setTimeout(function() {
          this.animating = false
        }.bind(this), 1000)
        this.nextCard()
      }
      if (e.deltaY < -1 * this.scrollThreshold && !this.animating && this.card > 1) {
        this.animating = true
        setTimeout(function() {
          this.animating = false
        }.bind(this), 1000)
        this.prevCard()
      }
    },
    nextCard () {
      window.Velocity(document.getElementById('card-' + this.card), {height: '0vh'}, 800)
      this.card++
    },
    prevCard () {
      this.card--
      window.Velocity(document.getElementById('card-' + this.card), {height: '100vh'}, 800)
    }
  },
  created () {
    window.addEventListener('wheel', this.handleScroll)
  },
  destroyed () {
    window.removeEventListener('wheel', this.handleScroll)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Roboto|Source+Sans+Pro|Ubuntu');

  .poster-container {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }

  .poster-card {
    width: 100vw;
    height: 100vh;
  }
  /*background-image: url('./images/poster_1.jpeg');
  background-repeat: no-repeat;
  background-size: cover;
  position: absolute;*/

  /* from material design */
  .shadow {
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);
  }

  .shadow:hover {
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  }
</style>

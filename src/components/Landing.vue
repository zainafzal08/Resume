<template>
  <div class="poster-container">
    <!-- With < max elements they need to hover near middle -->

    <DotNav :dotNum="cards.length" :trigger="updateCard" :selected="card"></DotNav>

    <Card name="card-1" suffix="-innards" bgc="#272B30">
      <TitleBrand title="Zain Afzal"></TitleBrand>
    </Card>

    <Card name="card-2" suffix="-innards" bgc="#444444">

    </Card>

    <Card name="card-3" suffix="-innards" bgc="#777777">

    </Card>
  </div>
</template>

<script>
import './js/velocity.js'
import DotNav from './DotNav.vue'
import TitleBrand from './TitleBrand.vue'
import Card from './Card.vue'

export default {
  name: 'Landing',
  data () {
    return {
      animating: false,
      cards: [
        ["card-1","card-1-innards"],
        ["card-2","card-2-innards"],
        ["card-3","card-3-innards"]
      ],
      card: 1,
      scrollThreshold: 15
    }
  },
  components: {
    DotNav,
    TitleBrand,
    Card
  },
  methods: {
    handleScroll (e) {
      if (e.deltaY > this.scrollThreshold && this.card <= this.cards.length ) {
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
      window.Velocity(document.getElementById(this.cards[this.card-1][0]), {'margin-top': '-100vh'}, d)
      this.card++
      window.Velocity(document.getElementById(this.cards[this.card-1][1]), {opacity: '1'}, d)
    },
    prevCard (d,ignoreState) {
      if (this.animating && !ignoreState) {
        return
      } else if (!ignoreState) {
        this.animating = true
        setTimeout(function() { this.animating = false }.bind(this), d+100)
      }
      window.Velocity(document.getElementById(this.cards[this.card-1][1]), {opacity: '0'}, d)
      this.card--
      window.Velocity(document.getElementById(this.cards[this.card-1][0]), {'margin-top': '0vh'}, d)
      window.Velocity(document.getElementById(this.cards[this.card-1][1]), {opacity: '1'}, d)
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

  /* Container  */
  .poster-container {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }

  /* poster background info */
  .BACKUP {
    background-image: url('./images/poster_1.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
  }
</style>

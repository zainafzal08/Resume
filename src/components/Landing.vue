<template>
  <div class="poster-container">
    <DotNav :bg="theme" :dotNum="cards.length" :trigger="updateCard" :selected="card" :focused="card == 1"></DotNav>

    <Card name="card-1" suffix="-innards" :bg="theme" bgt="color">
      <TitleBrand title="Zain Afzal"></TitleBrand>
    </Card>

    <Card name="card-2" suffix="-innards" :bg="require('./images/poster_1.jpeg')" bgt="image">
      <ProjectOutline title="Image Scrapers" :bg="theme" theme="#29ABE0" :points="cardData.imageScraper"></ProjectOutline>
    </Card>

    <Card name="card-3" suffix="-innards" :bg="theme" bgt="color">
      <ProjectOutline title="Web Dev" :bg="theme" theme="#29ABE0" :points="cardData.webDev"></ProjectOutline>
    </Card>

    <Card name="card-4" suffix="-innards" :bg="theme" bgt="color">
      <Footer :socialLinks="socials"></Footer>
    </Card>
  </div>
</template>

<script>
import DotNav from './DotNav.vue'
import TitleBrand from './TitleBrand.vue'
import Card from './Card.vue'
import ProjectOutline from './ProjectOutline.vue'
import Footer from './Footer.vue'

export default {
  name: 'Landing',
  data () {
    return {
      animating: false,
      cards: [
        ["card-1","card-1-innards"],
        ["card-2","card-2-innards"],
        ["card-3","card-3-innards"],
        ["card-4","card-4-innards"]
      ],
      socials: [
        {link: "https://github.com/zainafzal08", icon: "github-circle"},
        {link: "https://twitter.com/NubmerOneHo", icon: "twitter"},
        {link: "https://www.linkedin.com/in/zain-afzal-561262117/", icon: "linkedin"},
        {link: "mailto:zain.afz@gmail.com", icon: "email"}
      ],
      card: 1,
      scrollThreshold: 15,
      theme: "#272B30",
      cardData: {
        imageScraper:[
          {
            title: "Pixel Scraper",
            description: "A small script to search and find royalty free images from pexels landscape images.",
            links: [{link: "https://gogle.com", icon: "github-circle"}]
          },
          {
            title: "NatGeo Scraper",
            description: "A small script to search and find images from National Geographics Image Archives given constraints.",
            links: [{link: "https://gogle.com", icon: "github-circle"}]
          },
          {
            title: "Reddit Scraper",
            description: "A small script to search and find a beautiful image from reddit given constraints.",
            links: [{link: "https://gogle.com", icon: "github-circle"}]
          }
        ],
        webDev: [
          {
            title: "Hex Generator",
            description: "A simple javascript function that generates a tesselating hexgon pattern with a gradient. Helped me understand basic gradient generation algorithms",
            links: [{link: "https://codepen.io/zainafzal08/pen/EoqZVN", icon: "codepen"}]
          }
        ]
      }
    }
  },
  components: {
    DotNav,
    TitleBrand,
    Card,
    ProjectOutline,
    Footer
  },
  mounted: function(){
    for(var card in this.cards){
      if (card != 0)
        document.getElementById(this.cards[card][1]).style.opacity = '0';
    }
  },
  methods: {
    handleScroll (e) {
      if (e.deltaY > this.scrollThreshold && this.card < this.cards.length ) {
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
      window.Velocity(document.getElementById(this.cards[this.card-1][1]), {opacity: '0'}, d)
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
  /* Container  */
  .poster-container {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }
</style>

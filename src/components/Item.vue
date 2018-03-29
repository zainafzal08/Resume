<template>
  <div class="item-wrapper">
    <a :href="data.link">
      <div class="item">
        <div class="desc-wrapper">
          <h1> {{data.name}} </h1>
          <h2> {{data.sub}} </h2>
        </div>
        <div class="count-wrapper">
          <h3> {{data.count}} </h3>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: 'item',
  props: ["data"],
  data () {
    return {}
  },
  methods: {}
}
</script>

<style>
.item {
  margin-top: 1em;
  margin-bottom: 1em;
  padding: 1em;
  background-color: #3A3F44;
  text-align: left;
  color: white;
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
  cursor: pointer;
  display: flex;
}

.item .desc-wrapper {
  height: 100%;
  width: 80%;
}

.item .count-wrapper {
  width: 20%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.item-wrapper a{
  text-decoration: none;
  font-family: 'Ubuntu', sans-serif;

}
.item h1 {
  font-size: 1.2em;
}
.item h2 {
  font-size: 0.8em;
  color: #919aa1;
}
.item h3 {
  font-size: 1.1em;
  color: #919aa1;
}
.item:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}
</style>

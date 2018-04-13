<template>
  <div class="md-page">
    <div class="md-page-title">
      <h1> {{title}} </h1>
      <hr class="underline">
    </div>
    <div class="md-page-content">
      <div v-if="content == null" class="loading-dots">
        <pulse-loader :loading="loading" color="#919aa1"></pulse-loader>
      </div>
      <div v-if="content != null">
        <div v-html="content"></div>
      </div>
    </div>
  </div>
</template>

<script>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: 'markdownPage',
  props: ["content","title"],
  data () {
    return {}
  },
  components: {
    PulseLoader
  }
}
</script>

<style>
/*
 * Frankly a bit of a hack copying the hex color
 * theme should be universal
 */
.md-page {
  width: 100vw;
  text-align: center;
  font-family: 'Ubuntu',sans-serif;
}
.md-page .md-page-title {
    padding-top: 10vh;
    color: white;
}
.md-page .underline{
  border: 0;
  height: 3px;
  width: 75%;
  border-radius: 25px;
  background-color: #919aa1;
}

.md-page h1{
  font-size: 2.5rem;
  margin-top: 0;
}

.md-page .md-page-content {
  padding: 4em;
}

.md-page .md-page-content .loading-dots{
  text-align: center;
}
.md-page-content h1, h2, h3, h4, h5, h6, p, blockquote {
   margin: 0;
   padding: 0;
}
.md-page-content {
   font-family: 'Ubuntu',sans-serif;
   font-size: 13px;
   line-height: 18px;
   color: #fff;
   margin: 10px 13px 10px 13px;
}
.md-page-content table {
	 margin: 10px 0 15px 0;
	 border-collapse: collapse;
}
.md-page-content td,th {
	 border: 1px solid #ddd;
	 padding: 3px 10px;
}
.md-page-content th {
	 padding: 5px 10px;
}
.md-page-content a {
   color: #59acf3;
}
.md-page-content a:hover {
   color: #a7d8ff;
   text-decoration: none;
}
.md-page-content a img {
   border: none;
}
.md-page-content p {
   margin-bottom: 9px;
}
.md-page-content h1, h2, h3, h4, h5, h6 {
   color: #fff;
   line-height: 36px;
}
.md-page-content h1 {
   margin-bottom: 18px;
   font-size: 30px;
}
.md-page-content h2 {
   font-size: 24px;
}
.md-page-content h3 {
   font-size: 18px;
}
.md-page-content h4 {
   font-size: 16px;
}
.md-page-content h5 {
   font-size: 14px;
}
.md-page-content h6 {
   font-size: 13px;
}
.md-page-content hr {
   margin: 0 0 19px;
   border: 0;
   border-bottom: 1px solid #ccc;
}
.md-page-content blockquote {
   padding: 13px 13px 21px 15px;
   margin-bottom: 18px;
   font-family:georgia,serif;
   font-style: italic;
}
.md-page-content blockquote:before {
   content:"\201C";
   font-size:40px;
   margin-left:-10px;
   font-family:georgia,serif;
   color:#eee;
}
.md-page-content blockquote p {
   font-size: 14px;
   font-weight: 300;
   line-height: 18px;
   margin-bottom: 0;
   font-style: italic;
}

.md-page-content code, pre {
   font-family: Menlo, Monaco, Andale Mono, Courier New, monospace;
}

.md-page-content code {
   padding: 1px 3px;
   font-size: 12px;
   -webkit-border-radius: 3px;
   -moz-border-radius: 3px;
   border-radius: 3px;
   background: #334;
}

.md-page-content pre {
   display: block;
   padding: 14px;
   margin: 0 0 18px;
   line-height: 16px;
   font-size: 11px;
   border: 1px solid #334;
   white-space: pre;
   white-space: pre-wrap;
   word-wrap: break-word;
   background-color: #282a36;
   border-radius: 6px;
}

.md-page-content pre code {
   font-size: 11px;
   padding: 0;
   background: transparent;
}
.md-page-content sup {
   font-size: 0.83em;
   vertical-align: super;
   line-height: 0;
}
* {
	 -webkit-print-color-adjust: exact;
}
@media screen and (min-width: 914px) {
   .md-page-content {
      width: 854px;
      margin:10px auto;
   }
}
@media print {
	 .md-page-content body,code,pre code,h1,h2,h3,h4,h5,h6 {
		  color: black;
	 }
	 .md-page-content table, pre {
		  page-break-inside: avoid;
	 }
}

</style>

<template>
  <div>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성자 : {{ article?.username }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="onClick">DELETE</button>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ArticleContent',  // 게시글 내용
  props:{
    article: Object,
  },  
  methods:{
    onClick(){
      this.$store.commit()
      // if(this.article.username === this.username){
      //   axios({
      //     methods: 'delete',
      //     url: `${API_URL}/articles/${this.article.id}`
      //   })
      // }else{
      //   alert('자신이 작성한 글만 삭제 가능합니다!')
      // }
    }
  },

}
</script>

<style>

</style>
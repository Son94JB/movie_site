<template>
  <div>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ArticleContent',  // 게시글 내용
  components: {
  },
  data() {
    return {
      article: Object,
      name: '',
      content: '',
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods:{
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${ this.$route.params.id }/`,
      })
      .then((res) => {
        this.article = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
  }
}
</script>

<style>

</style>
<template>
  <div>
    <h1>{{actorDetail.name}}</h1>
  </div>
</template>

<script>
export default {
    name: 'ActorDetailView',
    computed: {
        actorDetail() {
            return this.$store.getters.actorDetail;
        },
    },
    created() {
        this.$store.dispatch('fetchActorDetail', this.$route.params.id);
    },
}
</script>

<style>

</style>
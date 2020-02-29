<template>
  <div>
    <span>首页信息</span>
    <div>{{info}}</div>
    <div>
      <el-button type="primary" class="btn-login" @click='logOut'>退出</el-button>
    </div>
  </div>
</template>

<script>

  import {homeinfo} from "../network/homeinfo";


  export default {
    name: "HomePage",
    data() {
      return {
        info: null,
        // cloakState: true

      }
    },
    created() {
      homeinfo().then((res) => {
        this.info = res
        // this.cloakState = false
        console.log(res)
      }).catch(err => {
        console.log(err)
      })
      // console.log(this.$store.state.token)
    },

    methods: {
      logOut() {
        sessionStorage.removeItem('token')
        this.$router.push('/login')
      }
    }
  }
</script>

<style scoped>

</style>
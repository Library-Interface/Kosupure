# Kosupure
コスプレ: Kosupure is a Social Media Platform for Cosplay

CustomUser made with the help of tutorial from Django: https://learndjango.com/tutorials/django-custom-user-model

using pillow


Levels of access: 
Guest - Public only access to feed and profiles
Logged-in: Ability to follow creators and participate in fan-page discussion board
Creator - ability to view 'adult'
Guest vs Logged-in vs Creator tri-chotamy


Going through some changes...


    <hr>
        <li v-for="(comment, index) in post.comments" :key="index">method 13: [[ comment['comment'] ]] </li>
        <button @click="loadMore" v-if="currentPage * maxPerPage < comments.length">load more</button>

            currentPage: 1,
            maxPerPAge: 3
            totalResults: 0,

        computed: {
            paginatedComments: function () {
                return this.comments.slice(0, this.currentPage * this.maxPerPage)
            },
            totalResults() {
                return Object.keys(this.comments).length
            },
            pageCount() {
                return Math.ceil(this.totalResults / this.maxPerPage)
            },
            pageOffest() {
                return this.maxPerPage * this.currentPage
            }
        }




            loadComments: function () {
                axios({
                    method: 'GET',
                    url: `/apis/v1/comments/`,
                    params: {
                        filter: this.filter,
                        type: this.selection,
                        page: this.page,
                        _limit: 3
                    }
                }).then(response => {
                    this.comments = response.data
                })
            },
            loadMoreComments: function () {
                axios({
                    method: 'GET',
                    url: '/apis/v1/comments/'
                }).then(response => {
                    this.comments.push(response.data.results[0])
                })
            },
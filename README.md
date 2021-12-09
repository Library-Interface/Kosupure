# Kosupure
コスプレ: Kosupure is a Social Media Platform for Cosplay

CustomUser made with the help of tutorial from Django: https://learndjango.com/tutorials/django-custom-user-model

using pillow


Levels of access: 
Guest - Public only access to feed and profiles
Logged-in: Ability to follow creators and participate in fan-page discussion board
Creator - ability to view 'adult'
Guest vs Logged-in vs Creator tri-chotamy
\

cut from an experiment in home app area

Vue.component('new-post', {
        data: {
            newPostWords = '',
            tags = '',
            pic = '',
            tags = '',
            user = [],
            selectedFile: null,
        },

        template: `
        <div>
            <input type="file" accept="image/jpeg" @change=onFileChanged>
            <input type="text" placeholder="New post" v-model="newPostWords">
            <input type="text" placeholder="Enter Tags" v-model="tags">
            <button @click="newPost">Make a new post</button>
        </div>
        `,

        methods: {
            onFileChanged (event) {
                this.selectedFile = event.target.files[0]
            },
            loadCurrentUser: function() {
                axios({
                    method: 'get',
                    url: '/apis/v1/currentuser/'
                }).then(response => {
                    this.user = response.data
                })
            },
            newPost: function () {
                axios({
                    method: 'post',
                    url: '/apis/v1/posts/',
                    headers: {
                        'X-CSRFToken': this.csrf_token
                    },
                    data: {
                        "user_name": this.user.id,
                        "description": this.newPostWords,
                        "pic": this.selectedFile,
                        "tags": this.tags
                    }
                }).then(response => {
                    this.newPostWords = ''
                    this.loadPosts()
                })
            }
        },
        created: function () {
            this.loadCurrentUser()
        },
        mounted: function () {
            this.csrf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value;
        }
}),
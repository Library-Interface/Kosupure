# Kosupure
コスプレ: Kosupure is a Social Media Platform for Cosplay

CustomUser made with the help of tutorial from Django: https://learndjango.com/tutorials/django-custom-user-model

using pillow


Levels of access: 
Guest - Public only access to feed and profiles
Logged-in: Ability to follow creators and participate in fan-page discussion board
Creator - ability to view 'adult'
Guest vs Logged-in vs Creator tri-chotamy
![kosupre1](https://user-images.githubusercontent.com/65050037/146998260-e51dd3a4-8dfe-48cb-ae24-7799545a6c7a.JPG)
![kosupre2](https://user-images.githubusercontent.com/65050037/146998270-fc9bea1c-2bd5-451e-8f7d-1089e18013b9.JPG)
![kosupre3](https://user-images.githubusercontent.com/65050037/146998649-3978cea1-52ee-4521-9440-810f62a2e2ec.JPG)
![kosupre4](https://user-images.githubusercontent.com/65050037/146998651-fdfc0025-377a-4045-b17d-e60ea26add5c.JPG)
![kosupre5](https://user-images.githubusercontent.com/65050037/146998655-0e696b2a-bad2-4adf-af0c-46267e2ab607.JPG)


Just in case this method doesn't work:

models: 

pic = models.ImageField(upload_to='static/images')

Vue.component('new-post', {
        delimiters: ['[[', ']]'],
        props: [ 'user', 'csrf_token' ],
        data: function () {
            return {
            newPostWords:  '',
            tags: '',
            pic: '',
            selectedFile: null,
            adult_content: true,
        }},
        template: `
        <form enctype="multipart/form-data">
            <textarea cols="100" rows="3" placeholder="Enter description of the image here (max length 800 characters)" v-model="newPostWords" required></textarea>
            <br>
            <span class="limiter">[[ charactersLeft ]]</span>
            <br>
            <textarea cols="100" rows="2" placeholder="Enter Tags for the image here (max length 400 characters)" v-model="tags"></textarea><br>
            <br>
            <span class="limiter">[[ charactersLeftTags ]]</span>
            <br>
            <input type="file" accept="image/*" @change=onFileChanged class="choosefile">
            <h2>This post is safe for kids (no blood, gore, etc): <input type="checkbox" id="checkbox" v-model="adult_content"><label for="checkbox">[[ adult_content ? 'Uncheck box to certify image is safe for kids': 'check box if image is for adults' ]]</label></h2>
            <button @click.prevent="newPost" class="submit">Submit</button>
        </form>
        `,
        methods: {
            onFileChanged (event) {
                console.log(event)
                this.selectedFile = event.target.files[0]
            },
            newPost: function () {
                let formData = new FormData()
                formData.append('user_name', this.user.id)
                formData.append('description', this.newPostWords)
                formData.append('pic', this.selectedFile)
                formData.append('tags', this.tags)
                formData.append('adult_content', this.adult_content)
                axios({
                    method: 'post',
                    url: '/apis/v1/posts/',
                    headers: {
                        'X-CSRFToken': this.csrf_token
                    },
                    data: formData
                }).then(response => {
                    this.newPostWords = ''
                    this.tags = ''
                    this.$emit("post-created")
                })
            }
        },
        computed: {
            charactersLeft: function () {
                let char = this.newPostWords.length, limit = 800
                return (limit - char) + " / " + limit + " " + "characters remaining"
            },
            charactersLeftTags: function () {
                let char1 = this.tags.length, limit = 400
                return (limit - char1) + " / " + limit + " " + "characters remaining"
            }
        }
})



heroku config:set DISABLE_COLLECTSTATIC=1

git push heroku main

heroku config:unset DISABLE_COLLECTSTATIC

heroku run python manage.py collectstatic
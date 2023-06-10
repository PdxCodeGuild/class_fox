
let app = Vue.createApp({
    data() {
        return {
            greeting: "Welcome to the Assignment Tracker!",
            assignments: [
                {name: "lab1", grade: 90}
            ],
            name: "",
            grade: "",
            average: 100
        }
    },
    methods: {
        addAssignment() {
            this.assignments.push({name: this.name, grade: this.grade})
            this.name = ""
            this.grade = ""
        },
        removeItem(index){
            this.assignments.splice(index, 1)
        },
        calculateAverage(){
            let total = 0
            for(let item of this.assignments){
                total += item.grade
            }
            this.average = total / this.assignments.length
        }
    },
    // watch allows us to keep an eye on a variable and watch for changes. If the variable changes, we can call a function
    watch: {
        // Name of watcher must be the same as the variable in data you are watching
        assignments: {
            handler() {
                this.calculateAverage()
            },
            deep: true
        }
    },
    // created will run when page loads
    created() {
        this.calculateAverage()
    }
})

app.mount("#app")

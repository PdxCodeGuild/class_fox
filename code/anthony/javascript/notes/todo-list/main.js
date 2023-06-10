
let todoList = Vue.createApp({
    data() {
        return {
            todoList: [],
            todoName: "",
            editingIndex: null
        }
    },
    methods: {
        addTodo() {
            this.todoList.push(this.todoName)
            this.todoName = ""
        },
        deleteTodo(index) {
            this.todoList.splice(index, 1)
        },
        editTodo(index){
            this.editingIndex = index
        },
        doneEditing(){
            this.editingIndex = null
        }
    },
    async created () {
        let todos = await axios.get("https://jsonplaceholder.typicode.com/todos/")
        for(let todo of todos.data){
            this.todoList.push(todo.title)
        }
    }
})

todoList.mount("#todoList")
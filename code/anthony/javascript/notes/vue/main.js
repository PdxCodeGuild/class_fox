let numberToPhrase = Vue.createApp({
    // Data stores all of our app level variables
    data() {
        return {
            number: 0,
            phrase: ""
        }
    },
    // Methods store all of our functions
    methods: {
        convertToPhrase() {
            // Use `this.` to access variables inside of data()
            let lookup = {
                1: "one",
                2: "two",
                3: "three",
                4: "four",
                5: "five",
                6: "six",
                7: "seven",
                8: "eight",
                9: "nine",
                10: "ten",
                11: "eleven",
                12: "twelve",
                13: "thirteen",
                14: "fourteen",
                15: "fifteen",
                16: "sixteen",
                17: "seventeen",
                18: "eighteen",
                19: "nineteen",
                20: "twenty",
                30: "thirty",
                40: "forty",
                50: "fifty",
                60: "sixty",
                70: "seventy",
                80: "eighty",
                90: "ninety"
            }

            let word = ""

            if(this.number in lookup){
                this.phrase = lookup[this.number]
            } else {
                word += lookup[Math.floor(this.number / 10) * 10] // 34 -> 30
                word += " - "
                word += lookup[this.number % 10] // 34 -> 4
                this.phrase = word
            }

        },
        someOtherFunction(){

        }
    }
})

numberToPhrase.mount("#number-to-phrase")




// ***********************************************************************












let app = Vue.createApp({
    data() {
        return {
            className: "Fox",
            daysOfWeek: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            isSunny: true,
            bgColor: "#ffffff"
        }
    },
    methods: {
        changeBG() {
            document.body.style.backgroundColor = this.bgColor
        }
    }
})

app.mount("#app")
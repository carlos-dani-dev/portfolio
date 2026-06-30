import { defineStore } from "pinia";

export const useLangStore = defineStore("lang", {
    state: () => ({
        lang: localStorage.getItem("lang") || "pt-br"
    }),
    getters: {
        currentLang: (state) => {
            console.log(state.lang)
            return state.lang
        }
    },
    actions: {
        setLang(newLang){
            this.lang = newLang
            localStorage.setItem("lang", newLang)
        }
    }
})
import { defineStore } from "pinia";
import { watch } from "vue";
import { useI18n } from "vue-i18n";


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
        },
        initLang(){
            const {locale} = useI18n()
            watch(
                () => this.lang,
                (val) => {locale.value = val },
                { immediate: true }
            )
        }
    }
})
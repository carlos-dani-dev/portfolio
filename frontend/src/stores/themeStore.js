import { defineStore } from "pinia";

export const useThemeStore = defineStore("theme", {
    state: () => ({
        isDark: localStorage.getItem("theme") === "dark-default"
    }),
    getters: {
        currentTheme: (state) => {
            if (state.isDark) return "dark-default"
            else return "light"
        }
    },
    actions: {
        changeTheme() {
            this.isDark = !this.isDark
            localStorage.setItem("theme", this.isDark ? "dark-default" : "light")
            document.documentElement.setAttribute("page-theme", this.isDark ? "dark-default" : "light")
            console.log(this.isDark)
        },
        initTheme() {
            const storedTheme = localStorage.getItem("theme")
            if (storedTheme === null) {
                this.isDark = true
                localStorage.setItem("theme", "dark-default")
            } else {
                this.isDark = storedTheme === "dark-default"
            }
            document.documentElement.setAttribute("page-theme", this.isDark ? "dark-default" : "light")
            console.log(this.isDark)
        }
    }
})
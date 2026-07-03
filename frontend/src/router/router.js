import { createRouter, createWebHistory } from 'vue-router';

import Home from '@/views/Home.vue';
import Resume from '@/views/Resume.vue';


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),

    routes: [
        { path: '/home', component: Home },
        { path: '/', redirect: '/home' },
        {path: '/home/resume', component: Resume}
    ]
})

export default router;
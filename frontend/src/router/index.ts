import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'


const routes: Array<RouteRecordRaw> = [
    {
        path: "/admin_news",
        name: "Home",
        component: () => import("../views/Home.vue"),
        children: [
            {path: "/", component: () => import("../views/Index.vue")},
            {path: "/admin_news/news", component: () => import("../views/news/newsList.vue")},
        ],
    },
    {
        path: "/admin_news/:catchAll(.*)",
        name: "404",
        component: () => import("../views/404.vue")
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
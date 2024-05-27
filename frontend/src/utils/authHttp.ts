import axios from 'axios'
import router from "../router";

const url = import.meta.env.VITE_APP_AUTH_API;

const api = axios.create({
    baseURL: url,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    },
});

// 請求攔截
api.interceptors.request.use((config: any) => {
    // token
    if (localStorage.token) {
        config.headers.Authorization = `Bearer ${localStorage.token}`
    }
    return config;
}, (error) => {
    return Promise.reject(error)
})

// 響應攔截
api.interceptors.response.use((response) => {
    return response;
}, (error) => {
    const {status, data, statusText} = error.response
    if (status === 401 || status === 403) {
        localStorage.removeItem("token")
        router.push('/admin_dealer/login')
    }
    if (400 <= status || status < 500) {
        // @ts-ignore
        ElMessage.error(`${data.message}`)
    }
    return Promise.reject(error)
})

export default api;
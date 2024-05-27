import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { VueClipboard } from '@soerenmartius/vue3-clipboard'
import {
    HomeFilled,
    Money,
    Warning,
    InfoFilled,
    ArrowDown,
    Timer,
    Goods,
    Search,
    User,
    Shop,
    ShoppingCart,
    Check,
    Close,
    Setting,
    Opportunity,
    CircleCloseFilled, CopyDocument,
} from '@element-plus/icons-vue'

const app = createApp(App)
const pinia = createPinia()

const icons = {
    "HomeFilled": HomeFilled,
    "Money": Money,
    "InfoFilled": InfoFilled,
    "ArrowDown": ArrowDown,
    "Timer": Timer,
    "Goods": Goods,
    "Search": Search,
    "Warning": Warning,
    "User": User,
    "Shop": Shop,
    "ShoppingCart": ShoppingCart,
    "Check": Check,
    "Close": Close,
    "Setting": Setting,
    "Opportunity": Opportunity,
    "CircleCloseFilled": CircleCloseFilled,
    "CopyDocument": CopyDocument,
}

for (const [key, value] of Object.entries(icons)) {
    app.component(key, value)
}

app.use(router)
app.use(pinia)
app.use(VueClipboard)
app.mount('#app')

import {defineStore} from 'pinia'
import {userType} from '../utils/types'
import {tabsType} from "../utils/types/tabs";

export const useAuthStore = defineStore('auth', {
    state: () => {
        return {isAuthenticated: false, user: {}}
    },
    getters: {
        getAuthenticated: (state) => state.isAuthenticated,
        getUser: (state) => state.user
    },
    actions: {
        setAuth(isAuth: boolean) {
            if (isAuth) {
                this.isAuthenticated = isAuth
            } else {
                this.isAuthenticated = false
            }
        },
        setUser(user: userType | null) {
            if (user) {
                this.user = user
            } else {
                this.user = {user_id: null, full_name: ''}
            }
        }
    },
})

export const useDynamicTabs = defineStore('tabs', {
    state: () => ({
        tabsArray: [] as tabsType[]
    }),
    getters: {
        getTabsArray: (state) => {
            return state.tabsArray
        }
    },
    actions: {
        setTabsArray(menuInfo: tabsType) {
            const result = this.tabsArray.filter((obj) => {
                    return obj.menuId === menuInfo.menuId
                }
            )
            if (result.length === 0) {
                this.tabsArray.push(menuInfo)
            }
        }
    },
})
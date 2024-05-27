import api from './http'


export function downloadFile(filename: string, data: any) {
    const downloadUrl = window.URL.createObjectURL(new Blob([data]))
    const link = document.createElement('a')
    link.href = downloadUrl
    link.setAttribute('download', filename)
    document.body.appendChild(link)
    link.click()
    link.remove()
}
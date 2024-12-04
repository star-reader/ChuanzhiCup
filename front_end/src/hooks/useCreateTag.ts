export default (tagstr: string) => {
    const tags = tagstr.replace(/，/g, ',').split(',')
    return tags
}
$(function () {
    function render_time() {
        // 獲取元素之 data-timestamp 屬性的內容
        return moment($(this).data('timestamp')).format('lll')
    }

    // tooltop() 的 title 屬性用來設置彈出區塊的內容
    $('[data-toggle="tooltip"]').tooltip({ title: render_time })
})
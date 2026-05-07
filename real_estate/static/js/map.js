ymaps.ready(init);


function init() {

    const map = new ymaps.Map('map', {
        center: [40.177200, 44.503490],
        zoom: 14,
        controls: ['zoomControl']
    });


    const PriceLayout = ymaps.templateLayoutFactory.createClass(
        `
        <div class="price-marker">
            {{ properties.iconContent }}
        </div>
        `
    );


    window.FLATS['data'].forEach(item => {

        const placemark = new ymaps.Placemark(
            [
                parseFloat(item.lat),
                parseFloat(item.lng)
            ],
            {
                iconContent: item.label,

                balloonContent: buildBalloon(item),
            },
            {
                iconLayout: 'default#imageWithContent',

                iconContentLayout: PriceLayout,

                iconImageHref:
                    'https://yastatic.net/s3/home-static/_/empty.png',

                iconImageSize: [1, 1],

                iconImageOffset: [0, 0],

                hideIconOnBalloonOpen: false,

                openBalloonOnClick: true,

                iconShape: {
                    type: 'Rectangle',
                    coordinates: [
                        [-60, -50],
                        [60, 0]
                    ]
                },

            }
        );

        map.geoObjects.add(placemark);

    });

}


function buildBalloon(item) {

    let html = `
        <div style="
            width:320px;
            max-height:500px;
            overflow:auto;
        ">
    `;


    item.data.forEach(flat => {

        html += `
            <div style="
                margin-bottom:16px;
                padding-bottom:16px;
                border-bottom:1px solid #eee;
            ">

                <img
                    src="https:${flat.img}"
                    style="
                        width:100%;
                        border-radius:12px;
                        margin-bottom:10px;
                        object-fit:cover;
                    "
                >

                <div style="
                    font-size:18px;
                    font-weight:700;
                    margin-bottom:6px;
                ">
                    ${flat.price}
                </div>

                <div style="
                    margin-bottom:6px;
                    line-height:1.4;
                ">
                    ${flat.title}
                </div>

                <div style="
                    color:#777;
                    font-size:14px;
                    margin-bottom:6px;
                ">
                    ${flat.attr}
                </div>

                <div style="
                    color:#1e98ff;
                    font-size:14px;
                    font-weight:600;
                ">
                    ${flat.clabel}
                </div>

                <a
                    href="https://www.list.am/item/${flat.id}"
                    target="_blank"
                    style="
                        display:inline-block;
                        margin-top:10px;
                        text-decoration:none;
                        color:#1e98ff;
                        font-weight:600;
                    "
                >
                    Открыть объявление
                </a>

            </div>
        `;

    });


    html += '</div>';

    return html;
}
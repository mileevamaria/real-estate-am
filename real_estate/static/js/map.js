import { initPolygon } from './polygon.js';

import { buildBalloon } from './balloon.js';


ymaps.ready(init);


function init() {

    const map = new ymaps.Map('map', {
        center: [40.177200, 44.503490],

        zoom: 14,

        controls: ['zoomControl'],

        behaviors: [
            'drag',
            'scrollZoom',
            'multiTouch',
        ]
    });


    // disable map zoom on double click

    map.behaviors.disable(
        'dblClickZoom'
    );


    const PriceLayout = ymaps
        .templateLayoutFactory
        .createClass(
            `
            <div class="price-marker">
                {{ properties.iconContent }}
            </div>
            `
        );


    window.FLATS.forEach(item => {

        const placemark = new ymaps.Placemark(
            [
                parseFloat(item.lat),
                parseFloat(item.lng)
            ],
            {
                iconContent: item.label,

                balloonContent:
                    buildBalloon(item),
            },
            {
                iconLayout:
                    'default#imageWithContent',

                iconContentLayout:
                    PriceLayout,

                iconImageHref:
                    'https://yastatic.net/s3/home-static/_/empty.png',

                iconImageSize: [1, 1],

                iconImageOffset: [0, 0],

                hideIconOnBalloonOpen: false,

                openBalloonOnClick: true,

                iconShape: {
                    type: 'Rectangle',

                    coordinates: [
                        [-60, -25],
                        [60, 25]
                    ]
                }
            }
        );

        map.geoObjects.add(placemark);

    });

    window.POLYGONS.forEach(geojson => {

        const feature =
            geojson.features[0];

        const polygonCoords =
            feature.geometry.coordinates;

        const polygon = new ymaps.Polygon(
            polygonCoords,
            {
                hintContent:
                    feature.properties.name
            },
            {
                fillColor:
                    'rgba(0, 255, 0, 0.15)',

                strokeColor:
                    '#00AA00',

                strokeWidth: 3,
            }
        );

        map.geoObjects.add(polygon);

    });


    initPolygon(map);

}
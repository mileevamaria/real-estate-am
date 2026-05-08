export function initPolygon(map) {

    let polygonCoords = [];

    let polygon = null;


    // =========================
    // Draw polygon
    // =========================

    map.events.add(
        'dblclick',
        function (e) {

            const target = e.get('target');


            // ignore placemarks

            if (target !== map) {
                return;
            }


            e.preventDefault();

            const coords = e.get('coords');

            polygonCoords.push(coords);


            // create polygon only once

            if (!polygon) {

                polygon = new ymaps.Polygon(
                    [polygonCoords],
                    {},
                    {
                        fillColor:
                            'rgba(0, 0, 255, 0.25)',

                        strokeColor:
                            '#0000FF',

                        strokeWidth: 3,

                        interactivityModel:
                            'default#transparent',
                    }
                );

                map.geoObjects.add(polygon);

            } else {

                polygon.geometry.setCoordinates([
                    polygonCoords
                ]);

            }

        }
    );


    // =========================
    // Controls
    // =========================

    const controls =
        document.createElement('div');


    controls.style.position = 'absolute';

    controls.style.top = '20px';

    controls.style.right = '20px';

    controls.style.zIndex = '9999';

    controls.style.background = '#ffffff';

    controls.style.padding = '16px';

    controls.style.borderRadius = '14px';

    controls.style.boxShadow =
        '0 4px 12px rgba(0,0,0,0.15)';

    controls.style.display = 'flex';

    controls.style.flexDirection = 'column';

    controls.style.gap = '10px';

    controls.style.width = '240px';


    // =========================
    // Input
    // =========================

    const input =
        document.createElement('input');


    input.type = 'text';

    input.placeholder =
        'Название полигона';

    input.style.padding = '10px';

    input.style.border =
        '1px solid #ddd';

    input.style.borderRadius = '10px';


    // =========================
    // Save button
    // =========================

    const saveButton =
        document.createElement('button');


    saveButton.innerText = 'Сохранить';

    saveButton.style.padding = '10px';

    saveButton.style.border = 'none';

    saveButton.style.borderRadius = '10px';

    saveButton.style.background =
        '#1e98ff';

    saveButton.style.color = '#fff';

    saveButton.style.cursor = 'pointer';


    // =========================
    // Reset button
    // =========================

    const resetButton =
        document.createElement('button');


    resetButton.innerText = 'Сбросить';

    resetButton.style.padding = '10px';

    resetButton.style.border = 'none';

    resetButton.style.borderRadius =
        '10px';

    resetButton.style.background =
        '#f1f1f1';

    resetButton.style.cursor = 'pointer';


    controls.appendChild(input);

    controls.appendChild(saveButton);

    controls.appendChild(resetButton);


    document
        .getElementById('map')
        .appendChild(controls);


    // =========================
    // Reset
    // =========================

    resetButton.addEventListener(
        'click',
        function () {

            if (polygon) {

                map.geoObjects.remove(
                    polygon
                );

                polygon = null;
            }

            polygonCoords = [];

        }
    );


    // =========================
    // Save
    // =========================

    saveButton.addEventListener(
        'click',
        async function () {

            if (
                polygonCoords.length < 3
            ) {

                alert('Min 3 точки');

                return;
            }


            if (
                !input.value.trim()
            ) {

                alert(
                    'Введи название полигона'
                );

                return;
            }


            const geojson = {
                type: 'FeatureCollection',

                features: [
                    {
                        type: 'Feature',

                        properties: {
                            name:
                                input.value.trim()
                        },

                        geometry: {
                            type: 'Polygon',

                            coordinates: [
                                polygonCoords
                            ]
                        }
                    }
                ]
            };


            const response = await fetch(
                polygonUrl,
                {
                    method: 'POST',

                    headers: {
                        'Content-Type':
                            'application/json'
                    },

                    body: JSON.stringify(
                        geojson
                    )
                }
            );


            const data =
                await response.json();


            alert(data.message);


            if (response.ok) {
                window.location.reload();
            }

        }
    );

}
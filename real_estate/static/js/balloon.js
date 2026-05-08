export function buildBalloon(item) {

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
                    ${flat.clabel || ''}
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
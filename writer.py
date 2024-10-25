from PIL import Image, ImageFont, ImageDraw


def writer_func(fullname, job, phone, email, site, address, company):
    img1 = Image.open(r'img.png')
    img2 = Image.open(r'img_1.png')

    # draw fg
    draw = ImageDraw.Draw(img1)
    # draw bg
    draw2 = ImageDraw.Draw(img2)

    print('started')

    # image size fg
    font1 = ImageFont.truetype("regular.ttf", 85)
    # image size fg
    font2 = ImageFont.truetype("regular.ttf", 35)

    # set fullname
    draw.text(
        (60, 50),
        fullname.title(), fill=(222, 177, 72, 148),
        font=font1,
    ),

    # set job
    draw.text(
        (60, 135),
        job.title(), fill=(222, 177, 72, 148),
        font=font1,
    ),

    # set phone
    draw.text(
        (120, 391),
        phone.title(), fill=(222, 177, 72, 148),
        font=font2,
    ),

    # set email
    draw.text(
        (120, 437),
        email.lower(), fill=(222, 177, 72, 148),
        font=font2,
    ),

    # set site
    draw.text(
        (120, 485),
        site.lower(), fill=(222, 177, 72, 148),
        font=font2,
    ),

    # set address
    draw.text(
        (120, 534),
        address.title(), fill=(222, 177, 72, 148),
        font=font2,
    ),

    # set company
    draw2.text(
        (55, 480),
        company.title(), fill=(222, 177, 72, 148),
        font=ImageFont.truetype("regular.ttf", 60),
    ),

    # img.show()
    img1.save(f'{fullname}1.png')
    img2.save(f'{fullname}2.png')
    print('Successfully is cut and saved')


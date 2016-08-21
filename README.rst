=================
instagram-explore
=================

.. image:: https://travis-ci.org/midnightSuyama/instagram-explore.svg?branch=master
    :target: https://travis-ci.org/midnightSuyama/instagram-explore

.. image:: https://badge.fury.io/py/instagram-explore.svg
    :target: https://badge.fury.io/py/instagram-explore

instagram scrapping module

------------
Installation
------------

::

    $ pip install instagram-explore

-----
Usage
-----

User
====

.. code-block:: python

   import instagram_explore as ie

   # Search user name
   res = ie.user('instagram')
   print(res.data)                   # All
   print(res.data['media']['nodes']) # Media list

   # Next page
   data, cursor = ie.user('instagram', res.cursor)

   # Image only
   images = ie.user_images('instagram').data

Tag
===

.. code-block:: python

   import instagram_explore as ie

   # Search tag name
   res = ie.tag('cat')
   print(res.data)                   # All
   print(res.data['media']['nodes']) # Media list

   # Next page
   data, cursor = ie.tag('cat', res.cursor)

   # Image only
   images = ie.tag_images('cat').data

Location
========

.. code-block:: python

   import instagram_explore as ie

   # Search location id
   res = ie.location('7226110')
   print(res.data)                   # All
   print(res.data['media']['nodes']) # Media list

   # Next page
   data, cursor = ie.location('7226110', res.cursor)

   # Image only
   images = ie.location_images('7226110').data

Media
=====

.. code-block:: python

   import instagram_explore as ie

   # Search media code
   res = ie.media('BFRO_5WBQfc')
   print(res.data)

   # Image only
   image = ie.media_image('BFRO_5WBQfc').data

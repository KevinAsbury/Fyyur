from app import db, Venue, Artist, Show

artist1 = Artist('Guns N Petals', 'San Francisco', 'CA', '326-123-5000', 
            'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80', 
            'https://www.facebook.com/GunsNPetals', 'https://www.gunsnpetalsband.com', True, 
            'Looking for shows to perform at in the San Francisco Bay Area!')

artist2 = Artist('Matt Quevedo', 'New York', 'NY', '300-400-5000', 
            'https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80', 
            'https://www.facebook.com/mattquevedo923251523', '', False)

artist3 = Artist('The Wild Sax Band', 'San Francisco', 'CA', '432-325-5432', 
            'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80', 
            '', '', False)

db.session.add_all([artist1, artist2, artist3])

venue1 = Venue('The Musical Hop', 'San Francisco', 'CA', '1015 Folsom Street', '123-123-1234', 
        'https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60', 
        'https://www.facebook.com/TheMusicalHop', 'https://www.themusicalhop.com', True, 
        'We are on the lookout for a local artist to play every two weeks. Please call us.')

venue2 = Venue('The Dueling Pianos Bar', 'New York', 'NY', '335 Delancey St', '914-003-1132', 
        'https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80', 
        'https://www.facebook.com/theduelingpianos', 'https://www.theduelingpianos.com', False)

venue3 = Venue('Park Square Live Music & Coffee', 'San Francisco', 'CA', '1017 Folsom Street', '415-000-1234', 
        'https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80', 
        'https://www.facebook.com/ParkSquareLiveMusicAndCoffee', 'https://www.parksquarelivemusicandcoffee.com', False)

show1 = Show(start_time = "2019-05-21T21:30:00.000Z")
show1.artist = artist1
venue1.shows.append(show1)

show2 = Show(start_time = "2019-06-15T23:00:00.000Z")
show2.artist = artist2
venue3.shows.append(show2)

show3 = Show(start_time = "2035-04-01T20:00:00.000Z")
show3.artist = artist3
venue3.shows.append(show3)

show4 = Show(start_time = "2035-04-08T20:00:00.000Z")
show4.artist = artist3
venue3.shows.append(show4)

show5 = Show(start_time = "2035-04-15T20:00:00.000Z")
show5.artist = artist3
venue3.shows.append(show5)

db.session.add_all([venue1, venue2, venue3])
db.session.commit()

# # create parent, append a child via association
# p = Parent()
# a = Association(extra_data="some data")
# a.child = Child()
# p.children.append(a)

# # iterate through child objects via association, including association
# # attributes
# for assoc in p.children:
#     print(assoc.extra_data)
#     print(assoc.child)
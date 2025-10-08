The infrastructure layer usually does not initiate action in the domain layer. Being “below” the domain
layer, it should have no specific knowledge of the domain it is serving. Indeed, such technical ca-
pabilities are most often offered as SERVICES. For example, if an application needs to send an e-
mail, some message-sending interface can be located in the infrastructure layer and the application
layer elements can request the transmission of the message. This decoupling gives some extra
versatility. The message-sending interface might be connected to an e-mail sender, a fax sender,
or whatever else is available. But the main benefit is simplifying the application layer, keeping it
narrowly focused on its job: knowing when to send a message, but not burdened with how.
The application and domain layers call on the SERVICES provided by the infrastructure layer. When
the scope of a SERVICE has been well chosen and its interface well designed, the caller can remain
loosely coupled and uncomplicated by the elaborate behavior the SERVICE interface encapsulates.
#pragma once

#include <string>

class Notification {
public:
    Notification() = default;
    
    /*
     * The "= 0" marks the function as virtual, which makes this class abstract.
     * 
     * A pure virtual function declares a function that inherited classes must implement
     * to become concrete classes. Here, every class that inherits Notification should
     * implement send(), though Notification itself does not provide a concrete implementation.
     * 
     * A class that contains at least one pure virtual function is considered abstract,
     * and we cannot instantiate an abstract class directly.
     
     * Here, we cannot instantiate Notification directly.
     * But it is still possible to use Notification* pointer for
     * inherited classes like EmailNotification.
     */
    virtual void send(std::string message) = 0;
};
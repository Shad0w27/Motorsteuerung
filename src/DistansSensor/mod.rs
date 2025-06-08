pub struct DistanceSensor {
    pub trigPin: u32,
    pub echoPin: u32,
    pub value: f32,
}

impl DistanceSensor {
    pub fn new(id: u32) -> Self {
        DistanceSensor { id, value: 0.0 }
    }

    pub fn read_value(&self) -> f32 {
        self.value
    }

    pub fn set_value(&mut self, value: f32) {
        self.value = value;
    }
}
